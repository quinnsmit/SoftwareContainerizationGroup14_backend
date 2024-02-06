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

### Object-Relational Mapping (ORM) library SQLAlchemy
* pip install flask-sqlalchemy


### kubernetes

#### build flask image
`docker build -t python-app -f Dockerfile .`

#### tag the build image
`docker tag f6d43c61a64f 172.22.154.178:32000/python-app-dev`

#### docker push
`docker push 172.22.154.178:32000/python-app-dev`

#### k8s apply deployment
`microk8s kubectl apply -f flask-deployment.yml`

#### Portforward 
`MICROK8S kubectl port-forward flaskapi-deployment-59cc79b6c4-kfc58 8080:5000`

#### K8S logs
`microk8s kubectl logs -f flaskapi-deployment-67b67c7fb-tlm22`

#### K8s delete deploy
`microk8s kubectl delete -n default deployment flaskapi-deployment`

