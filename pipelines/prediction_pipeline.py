import pickle
import pandas as pd


class PredictionPipeline:
    def __init__(self):
        with open("notebooks/artifacts/customer_segmentation_pipeline.pkl", "rb") as f:
            self.model = pickle.load(f)

    def predict(self, input_data: dict):
        """
        input_data: dict with feature_name -> value
        """
        df = pd.DataFrame([input_data])
        prediction = self.model.predict(df)
        return int(prediction[0])

    def predict_with_info(self, input_data: dict):
        """
        Returns cluster id plus centroid distance and confidence score.
        """
        df = pd.DataFrame([input_data])
        prediction = self.model.predict(df)
        distances = self.model.transform(df)[0]
        cluster = int(prediction[0])
        confidence = round(100 * (1 - distances[cluster] / (distances.sum() + 1e-9)), 2)

        return {
            "cluster": cluster,
            "distances": distances.tolist(),
            "confidence": confidence,
        }
