# Favorite CI/CD system voting

Simple voting web application built on Django framework and using PostgreSQL database for persistence.

Shows how to integrate with different CI/CD tools in order to build and deploy the app on Heroku.

## Deploy on Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/cpoenisch/cicd-voting/)

## Develop with Docker

- Rename *.env.sample* to *.env*
- Update the environment variables in *.env* file
- Build the images and run the containers:

  ```sh
  docker-compose up -d
  ```

Browse [localhost:8000](http://localhost:8000)

## License

[MIT](LICENSE)

## Credits

[lfbatista/movies_project](https://github.com/lfbatista/movies_project)
