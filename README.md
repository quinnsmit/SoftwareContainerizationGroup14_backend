# Database
quick instruction on how to run the database in docker.
### To build the db image
`docker build -t sc_database .`

### To run the db image
`docker run -p 3306:3306 --name SC_database_container -d sc_database`