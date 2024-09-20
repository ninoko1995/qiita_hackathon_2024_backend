DIRS=`find ./ -depth 1 -type d -not -path '*.git*' -not -path '*__pycache__*'`
FILES=`find ./ -depth 1 -type f -not -path '*.git*' -not -path '*/__pycache__/*'`

ssh:
	ssh miyablo@miyablo.sakura.ne.jp

upload:
	scp -r $(DIRS) $(FILES) miyablo@miyablo.sakura.ne.jp:~/www/kosugiiz

upload/repo:
	scp -r repository miyablo@miyablo.sakura.ne.jp:~/www/kosugiiz

upload/target:
	scp -r $(TARGET) miyablo@miyablo.sakura.ne.jp:~/www/kosugiiz