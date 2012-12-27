ERROR_PAGES := $(wildcard [0-9][0-9][0-9]*.html)
ERROR_FILES := $(patsubst %.html,%.http,$(ERROR_PAGES))

all: $(ERROR_FILES)

%.http: %.html
	python make-error-page.py $< > $@

504.reallydown.http: 504.reallydown.html
	python make-error-page.py --no-compress $< > $@

clean:
	rm -f $(ERROR_FILES)
