#!/bin/bash

if [ $1 == 'sucesso' ]
then
	curl -X POST -H 'Content-type: application/json' --data '{"text":"deu tudo certo na pipeline!"}' https://hooks.slack.com/services/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
else
	curl -X POST -H 'Content-type: application/json' --data '{"text":"algo deu errado na pipeline"}' https://hooks.slack.com/services/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
fi