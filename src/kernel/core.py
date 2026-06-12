class GenesisKernel:
    def __init__(self):
        self.modules = []

    def register_module(self, module_name):
        self.modules.append(module_name)
        print(f"Module registered: {module_name}")

    def start(self):
        print("Genesis AGI Core Started")
        print("Loaded modules:")
        for module in self.modules:
            print(f"- {module}")


kernel = GenesisKernel()

kernel.register_module("Memory")
kernel.register_module("Goals")
kernel.register_module("Decision")

kernel.start()
