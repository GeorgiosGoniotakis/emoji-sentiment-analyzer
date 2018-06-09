#run-unit:
.SILENT:

code-analysis:
	bash scripts/validate.sh

package:
	source activate /anaconda3/envs/emoji/ && pip freeze > requirements.txt && source deactivate


