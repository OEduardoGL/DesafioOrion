#!/bin/bash

# Função para mover arquivos com base no formato
move_files() {
  local src_path=$1
  local rel_path=$2
  local filename=$(basename "$src_path")

  if [[ $filename == *.csv ]]; then
    target_dir="/datalake/staging/csv/$rel_path"
  elif [[ $filename == *.xml ]]; then
    target_dir="/datalake/staging/xml/$rel_path"
  elif [[ $filename == *.html ]]; then
    target_dir="/datalake/staging/html/$rel_path"
  elif [[ $filename == *.json ]]; then
    target_dir="/datalake/staging/json/$rel_path"
  else
    return
  fi
  
  hdfs dfs -mkdir -p $target_dir  # Cria o diretório de destino se não existir
  hdfs dfs -mv $src_path $target_dir/  # Move o arquivo para o diretório de destino
}

process_directory() {
  local current_path=$1
  local rel_path=$2
  
  for item in $(hdfs dfs -ls $current_path | tail -n +2 | awk '{print $8}'); do
    local item_name=$(basename "$item")
    local new_rel_path="$rel_path/$item_name"
    
    if hdfs dfs -test -d $item; then
      process_directory $item $new_rel_path
    else
      move_files $item $rel_path
    fi
  done
}

main() {
  while true; do
    for dir in $(hdfs dfs -ls /datalake/raw | tail -n +2 | awk '{print $8}'); do
      if hdfs dfs -test -d $dir; then
        process_directory $dir $(basename $dir)
      else
        move_files $dir ""
      fi
    done
    sleep 30
  done
}

main