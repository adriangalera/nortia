venv:
	python3 -m venv .venv

install:
	PYTHONPATH=.venv ; . .venv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt

test:
	python -m unittest -v

lint:
	PYTHONPATH=.venv ; . .venv/bin/activate && pylint nortia

install-service:
	sudo cp nortia.service /etc/systemd/system/nortia.service
	sudo chmod 644 /etc/systemd/system/nortia.service
	sudo chown root:root /etc/systemd/system/nortia.service
	sudo systemctl enable nortia
	sudo systemctl start nortia

clean:
	rm -rf tests/repo-files && mkdir tests/repo-files

coverage:
	coverage run
	coverage report
	coverage xml

reset-hours-file:
	rm time-tracking.csv && touch time-tracking.csv