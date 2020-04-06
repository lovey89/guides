FROM openjdk:jdk-alpine

COPY target/hello-world-jar-1.0-SNAPSHOT.jar /deployments/

# Print java version and run the jar
CMD java -version && java -jar /deployments/hello-world-jar-1.0-SNAPSHOT.jar