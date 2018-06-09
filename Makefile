#run-unit:
.SILENT:

code-analysis:
	echo "========== Pylint Output ==========\n"
	pylint source
	echo "========== End of Pylint Output ==========\n"
	#pycodestyle source

package:
	source activate /anaconda3/envs/emoji/ && pip freeze > requirements.txt && source deactivate