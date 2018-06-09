#run-unit:
.SILENT:
PYLINT = pylint
PYLINTFLAGS = -rn

code-analysis:
	bash scripts/validate.sh

package:
	source activate /anaconda3/envs/emoji/ && pip freeze > requirements.txt && source deactivate


