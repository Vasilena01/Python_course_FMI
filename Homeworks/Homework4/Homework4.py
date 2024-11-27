class Material:
    density = 0
    def __init__(self, weight):
        self.weight = weight
    
    @property
    def volume(self):
        return self.weight / self.density

    def _get_class_name(self):
        return self.__class__.__name__


class Concrete(Material):
    density = 2500
    
    
class Brick(Material):
    density = 2000


class Stone(Material):
    density = 1600


class Wood(Material):
    density = 600


class Steel(Material):
    density = 7700


class Factory:
    created_material_classes = {
        "Brick": Brick,
        "Concrete": Concrete,
        "Steel": Steel,
        "Stone": Stone,
        "Wood": Wood,
    }
        
    used_instances = set()
    all_instances = set()

    def __init__(self):
        self.current_instances = set()
    
    def _get_base_densities(self, args, processed_classes):
        """Get the densities of the base materials used to create the given instances."""
        densities = []

        for arg in args:
            if isinstance(arg, Material):
                class_name = arg._get_class_name()
                base_classes = class_name.split("_")

                for base in base_classes:
                    if base not in processed_classes:
                        if base in self.created_material_classes:
                            densities.append(self.created_material_classes[base].density)
                            processed_classes.add(base)
                        else:
                            raise ValueError(f"Unknown material base: {base}")
        return densities

    def __call__(self, *args, **kwargs):
        if not args and not kwargs:
            raise ValueError("Cannot call with no arguments.")
        if args and kwargs:
            raise ValueError("Cannot mix positional and keyword arguments.")
        
        if kwargs:
            instances = ()
            for key, value in kwargs.items():
                if key in self.created_material_classes:
                    material_class = self.created_material_classes[key]
                    instance = material_class(value)
                    instances += (instance,)
                    
                    self.current_instances.add(instance)
                    self.all_instances.add(instance)
                else:
                    raise ValueError(f"Invalid name of keyword argument: {key}")
            return instances
        
        if args:
            for arg in args:
                if arg in self.used_instances:
                    raise AssertionError(f"Instance {arg} has already been used.")
                if not any(isinstance(arg, cls) for cls in self.created_material_classes.values()):
                    raise ValueError(f"Invalid material instance: {arg}")
            
            class_name = "_".join(
                sorted(
                    set(
                        base_name
                        for arg in args
                        for base_name in arg._get_class_name().split("_")
                    )))            
            
            if class_name in self.created_material_classes:
                dynamic_class = self.created_material_classes[class_name]
            else:
                processed_classes = set()
                base_densities = self._get_base_densities(args, processed_classes)
                average_density = sum(base_densities) / len(base_densities)

                dynamic_class = type(
                    class_name,
                    (Material,),
                    {
                        "density": average_density,
                    },
                )

                self.created_material_classes[class_name] = dynamic_class
                
            self.used_instances.update(args)
            total_weight = sum(arg.weight for arg in args)
            instance = dynamic_class(total_weight)
            
            self.current_instances.add(instance)
            self.all_instances.add(instance)
            
            return instance
        
    def can_build(self, required_volume):
        total_volume = sum(
            instance.volume
            for instance in self.current_instances
            if instance not in self.used_instances
        )
        return total_volume >= required_volume
    
    @classmethod
    def can_build_together(cls, required_volume):
        total_volume = sum(
            instance.volume
            for instance in cls.all_instances
            if instance not in cls.used_instances
        )
        return total_volume >= required_volume