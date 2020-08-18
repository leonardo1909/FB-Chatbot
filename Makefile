database:
	docker stop fb-message || true;
	docker container rm fb-message || true;
	docker run --rm --name fb-message -p 5432:5432 -e POSTGRES_PASSWORD=123 -e POSTGRES_DB=fb-message -d postgres;