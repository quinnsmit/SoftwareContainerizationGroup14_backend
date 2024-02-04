# Use the official MySQL image from Docker Hub
FROM mysql:latest

# Set environment variables for MySQL
ENV MYSQL_ROOT_PASSWORD=root
ENV MYSQL_DATABASE=SC_Group14
ENV MYSQL_USER=admin
ENV MYSQL_PASSWORD=admin

# Copy the schema.sql file to the /docker-entrypoint-initdb.d/ directory
#COPY ./schema.sql /docker-entrypoint-initdb.d/

# Expose the MySQL port
EXPOSE 3306


