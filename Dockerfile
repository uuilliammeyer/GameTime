FROM python:3.9

# Install the function's dependencies using file requirements.txt
# from your project folder.
# I may need a workdir
# copy all the files to the container
WORKDIR /usr/

COPY . .

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD [ "python", "src/main.py" ]