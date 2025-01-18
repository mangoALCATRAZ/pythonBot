# beanbot

### How to set up for development on your local machine

1. Install Python 3 and ensure you can access python3 from your terminal

2. Set up the Python 3 virtual enviornment in order to install project dependancies. This creates a dedicated project environment with all the code libraries needed for the project installed within it. In order to create the environment, run the following:

```
python3 -m venv myenv
```

And each time you are ready to run it, run this:

```
source myenv/Scripts/activate
```

You should see the environment name in parenthesis next to your name in the Terminal in paranthesis like so (venv)

Next, install the project's dependancies into the virtual environment, from the list of requirements.txt:

```
pip install -r requirements.txt
```

3. Finally, open up in your favorite IDE! :D
