## To Start the project

            docker-compose exec db psql --username=hello_django --dbname=hello_django_dev   ---> create database
            docker-compose up -d --build   ---> build the container and start it
            docker-compose down -v         ---> take down the container and associated volume
            docker-compose -logs -f        ---> view your logs
            docker volume inspect djdocker_postgres_data   ---> check that postgres volumes where created
