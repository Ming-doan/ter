# Import ter + page component
from ter import Ter, Config, import_support
from component import Home, Form, Info, Invalid

# Create app variable
app = Ter(config=Config(default_pause_message="Press Enter to continue..."))

# required: Register app routes object
# Route elements must be component
app.register_routes({
    'home': Home,
    'form': Form,
    'info': Info,
    'invalid': Invalid
})
import_support.set_app(app=app)

# Run this app
app.run()
