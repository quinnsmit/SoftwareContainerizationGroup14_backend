# Database
quick instruction on how to run the database in docker.
### To build the db image
`docker build -t sc_database .`

### To run the db image
`docker run -p 3306:3306 --name SC_database_container -d sc_database`

### Env variables of the database:
* MYSQL_ROOT_PASSWORD=root
* MYSQL_DATABASE=SC_Group14
* MYSQL_USER=admin
* MYSQL_PASSWORD=admin`


### REST API
* pip install flask
Object-Relational Mapping (ORM) library SQLAlchemy
* pip install flask-sqlalchemy
