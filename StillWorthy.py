class Service:
    """
    I haven't done Python for a while,
    had to see if I could still write it.
    A list where you can add services, the class will count them for you
    """
    running_services = 0
    services_list=[]
    def __init__(self,name):
        self.name = name
        Service.add_service(self.name)
    @classmethod
    def list_services(cls):
    """returns a list of service names"""
        for items in cls.services_list:
            return items
    @classmethod
    def add_service(cls,name):
    """counts one up and appends service name to list"""
        cls.running_services+=1
        cls.services_list.append(name)
    # TODO remove_service method
if __name__ == "__main__":
    # Just an example:
    mail = Service("E-Mail Server")
    print(f"There are currently {Service.running_services} running services\n",Service.services_list)
