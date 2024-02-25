from terapp import Component, import_support, Header
from state import store


class Home(Component):
    # required: Local state variable
    def __init__(self): ...

    # required: App will render this first
    def render(self, context):
        print(Header(context, "Home", 20, "strikethrough"))
        print("1. Fill in the form")
        print("2. Show info")
        print("3. Exit")

    # optional: Prompt message when paused
    def prompt(self):
        return "Select your choice: "

    # optional: Logic block, run after enter inputs
    def logic(self, command, context):
        if command == "1":
            context.navigate("form")
        elif command == "2":
            context.navigate("info")
        elif command == "3":
            import_support.current_app.exit()
        else:
            context.navigate("invalid")


class Form(Component):
    def __init__(self): ...

    def render(self, context):
        print("This is form")
        print("Please fill amount")

    def prompt(self):
        return "Amount: "

    def logic(self, command, context):
        store.dispatch(reducer="increase_by_amount", payload=int(command))
        context.navigate('home')


class Info(Component):
    def __init__(self): ...

    def render(self, context):
        print("This is info")
        print(f"The amount: {store.state}")

    def logic(self, command, context):
        context.navigate('home')


class Invalid(Component):
    def __init__(self):
        pass

    def render(self, context):
        print(Header(context, "Invalid input"))

    def logic(self, command, context):
        context.navigate('home')
