from flask import Flask, render_template

app = Flask(__name__)


def get_endpoint_port(endpoint):
    # Mapping endpoints to ports
    endpoint_ports = {
        '/': 5000,        # Home route
        '/home': 5000,
        '/about': 5001,
        '/contact': 5001,
        # Add more endpoint-to-port mappings as needed
    }
    return endpoint_ports.get(endpoint, 5000)  # Default to 5000 if not found


@app.before_request
def before_request():
    if request.endpoint:
        endpoint = request.endpoint
        view_function = app.view_functions.get(endpoint)
        if view_function:
            # Get the route from the view function
            route = app.url_map.iter_rules(endpoint).__next__().rule
            target_port = get_endpoint_port(route)
            
            # If the request is not on the correct port, redirect
            if request.environ.get('SERVER_PORT') != str(target_port):
                return redirect(f'http://{request.host.split(":")[0]}:{target_port}{request.path}')

@app.route("/")
def home():
    return "Home Page on Port 5000"


@app.route("/about")
def about():
    return "About Page on Port 5001"

@app.route('/contact')
def contact():
    return "Contact Page on Port 5001"
