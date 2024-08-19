import os
import logging
import pandas as pd

class ValidatorGadget:
    
    def __init__(self):
        self.mapping = self.load_validator_mapping()
    
    def _download_validator_mapping(self):
        df = pd.read_parquet("https://storage.googleapis.com/public_eth_data/openethdata/validator_data.parquet.gzip")
        df["validator_id"] = df["validator_id"].astype(int)  
        df.to_parquet("validator_mapping.parquet", index=False)
        logging.info("Validator mapping downloaded and stored to `./validator_mapping.parquet`")
    
    def _build_validator_mapping(self):
        
        validators = self.load_validators_locally()
        
        self.add_coinbase_validators()
        
        self.add_kiln_validators()
        
        self.add_binance_validators()
        
        self.add_rocketpool_validators()
        
        
    def _add_coinbase_validators(self):
        pass

    def _add_kiln_validators(self):
        pass

    def _add_binance_validators(self):
        pass

    def _add_rocketpool_validators(self):
        pass
        
        
    def load_validator_mapping(self):
        if not os.path.isfile("validator_mapping.parquet"):
            logging.warning("No validator mapping found locally")
            self._download_validator_mapping()
            return self.load_validator_mapping()
        return pd.read_parquet("validator_mapping.parquet")
         