USR_DIR=/content/prob
PROBLEM=wiki_sql
DATA_DIR=/content/data
TMP_DIR=/content/temp_dir
mkdir -p $TMP_DIR

t2t-datagen \
  --t2t_usr_dir=$USR_DIR \
  --data_dir=$DATA_DIR \
  --tmp_dir=$TMP_DIR \
  --problem=$PROBLEM
