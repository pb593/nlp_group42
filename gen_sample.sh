USR_DIR=our_problem
PROBLEM=wiki_sql
DATA_DIR=data/col_index
TMP_DIR=tmp
mkdir -p $TMP_DIR

t2t-datagen \
  --t2t_usr_dir=$USR_DIR \
  --data_dir=$DATA_DIR \
  --tmp_dir=$TMP_DIR \
  --problem=$PROBLEM
