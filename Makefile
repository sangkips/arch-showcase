# Give an image name
IMAGE=sangkips/arch:latest

# Build the image 
build:
	docker build -t $(IMAGE) .

# Start docker image in a detached mode
up:
	docker-compose up -d

# Show running docker containers 
ps:
	docker-compose ps 

# Run django migrations and migrate
migrate:
	docker-compose exec app python manage.py migrate

makemigrations:
	docker-compose exec app python manage.py makemigrations

# Handle and collect static files such as images 
collectstatic:
	docker-compose exec app python manage.py collectstatic --noinput

# Create a superuser account 
createsuperuser:
	docker-compose exec app python manage.py createsuperuser

# Show given logs 
logs:
	docker-compose logs -f

# Remove the container 
rm: stop
	docker-compose rm -f
	
# Stop container 
stop:
	docker-compose stop