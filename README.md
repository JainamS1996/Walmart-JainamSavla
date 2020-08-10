# Walmart-JainamSavla

1. What other information would you add to health endpoint json object in step 2? Explain what would be the use case for that extra information?

Extra Information added : Current Directory, User and HostName

Current Directory : What part of the application is being checked? (Eg - Is the database,backup and the application running? ) </br>
User : Identity and Access Management (Is the user authorized and authenticated, who performed the latest health check) </br>
HostName : Connectivity Test </br>
Disk Utilization : Monitoring the Disk Utilization (Scaling and Performance)


2. Create a docker file to build, package, deploy, and run this application locally with Docker.

## Building and Running Docker Application

Change your directory to app
```cd app```

Build the Dockerfile
```docker build -t jainam .```

Run the application 
```sudo docker run --name walmart --hostname test  -p 80:80 jainam```

<img width="1792" alt="Docker" src="https://user-images.githubusercontent.com/47433763/89779754-0c2b9880-dade-11ea-8525-73dab8358e6a.png">

<p align="center"> <br> Figure : Dockerized Flask Application with logs </br> </p>

3. How would you automate the build/test/deploy process for this application?</br>

What branching strategy would you use for development? </br>
Using GitHub or GitLab, create a branch of the central code whenever you need to add or update a feature. Each branch is the copy of the source code which allows us to edit,stage and commit to the feature branch. Once I have created a new development branch and done implementing/modifying the feature, I will merge those changes back into the master branch. This is sometimes called as Feature Branching.

What CICD tool/service would you use? </br>
Jenkins or Gitlab. For this application, I have used Jenkins.

What stages would you have in the CICD pipeline? </br>
- Adding the source as GitHub
- Build 
- Test

What would be the purpose of each stage in CICD pipeline </br>

- Getting the Source File from GitHub
- Building a customized docker image of Jenkins with dockerfile
- Building image of our application
- Unit testing and test reports in JUnit format

## Purpose
In a real world scenario, we work on a particular branch. Clone the repository to get the source. Building Stage - After we are done building and running the application on the local machine, we need to test the application, if it will for all the test case scenarios. QA further tests the application in the development stage before deploying it on the Production Server.

## Steps 

<img width="1792" alt="Source" src="https://user-images.githubusercontent.com/47433763/89785520-8bbe6500-dae8-11ea-9e71-40af4740afde.png">
<p align="center"> <br> Figure : Adding the source as GitHub </br> </p>

- Customized Docker Image of Jenkins with JenkinsDockerfile
``` docker build -t jenkins-docker-image -f JenkinsDockerfile .   ```

- Run the docker image of Jenkins
```docker run -d -p 8080:8080 --name jenkins-docker-container -v /var/run/docker.sock:/var/run/docker.sock jenkins-docker-image ```

- Unlock Jenkins
```docker exec -it jenkins-docker-container cat var/jenkins_home/secrets/initialAdminPassword```

- Create a new job on Jenkins

- Building flask application 

<img width="1792" alt="Build image and running flask application" src="https://user-images.githubusercontent.com/47433763/89786211-94636b00-dae9-11ea-9e16-ba615a9c8493.png">
<p align="center"> <br> Figure : Build Flask Application </p>

<img width="1789" alt="Screen Shot 2020-08-10 at 9 45 22 AM" src="https://user-images.githubusercontent.com/47433763/89789178-400eba00-daee-11ea-89ea-e46c575adc45.png">
<p align="center"> <br> Figure : Run Tests </p>

<img width="1792" alt="Success" src="https://user-images.githubusercontent.com/47433763/89787991-764b3a00-daec-11ea-9c19-a9dbc0e98240.png">
<p align="center"> <br> Figure : Build Success </p>









