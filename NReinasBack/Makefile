prod:
	docker compose -f docker-compose-prod.yml build --force-rm && docker compose -f docker-compose-prod.yml up --force-recreate -d && docker compose -f docker-compose-prod.yml run nreinas
uat:
	docker compose -f docker-compose-uat.yml build --force-rm && docker compose -f docker-compose-uat.yml up --force-recreate -d && docker compose -f docker-compose-uat.yml run nreinas
sit:
	docker compose -f docker-compose-sit.yml build --force-rm && docker compose -f docker-compose-sit.yml up --force-recreate -d && docker compose -f docker-compose-sit.yml run nreinas

