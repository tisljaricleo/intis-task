FROM tensorflow/serving

COPY ./models/model_agumeted/ /models/model_agumeted
COPY ./models/model_basic_data/ /models/model_basic_data

COPY ./config.conf /config/config.conf

ENV MODEL_CONFIG_FILE=/config/config.conf