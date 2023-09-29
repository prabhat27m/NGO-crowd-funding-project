from thirdweb import ThirdwebSDK
from thirdweb.types import SDKOptions
# sdk = ThirdwebSDK("goerli" , options=SDKOptions(secret_key="85e6aa516f0e766cb91fe58b133e6e9c9bacf10499fb1015789160bd6051f63f"))
sdk = ThirdwebSDK.from_private_key(
    "0x85e6aa516f0e766cb91fe58b133e6e9c9bacf10499fb1015789160bd6051f63f",
    "goerli",
    SDKOptions(secret_key="B7Ycjj2MYeZd8Iw3i0FIemslMBime6RBU8Wbfijoah2Ka6Hp_PKTKrGuRtu8TM9VYLCODrNtiuevsyo_14myTQ")
)
# sdk = ThirdwebSDK(network="goerli",options=SDKOptions(secret_key="B7Ycjj2MYeZd8Iw3i0FIemslMBime6RBU8Wbfijoah2Ka6Hp_PKTKrGuRtu8TM9VYLCODrNtiuevsyo_14myTQ"))
contract = sdk.get_contract("0xDd233FC710Bd600e735eC0DD5917c25c89d6cd78")
# print(sdk.get_signer())
# 85e6aa516f0e766cb91fe58b133e6e9c9bacf10499fb1015789160bd6051f63f
# sdk.update_signer("LocalAccount")
# data = contract.call("createCampaign", "0xBc1fBbd191AC64eD446BC982a628f5ef607e89a7", "Education", "give me money", 1, 7, "")
data = contract.call("getCampaigns")
# data = contract.call("getDonators", 2)
print(data)

# import FL from Flask
# app = Flask()
# def is_check_whether_fraud_campaign():
    
    
# app.route("/create")
# def create_campaign(.., paramater):
# ek kaam karo ki 


# from flask import Flask, request, jsonify
# import pandas as pd
# import pickle  # To load the trained machine learning model

# app = Flask(__name__)

# # Load the trained model
# model = pickle.load(open("fraud_detection_model.pkl", "rb"))  # Replace with your model file

# @app.route("/predict_fraud_percentage", methods=["POST"])
# def predict_fraud_percentage():
#     try:
#         # Get campaign data from the request
#         data = request.json

#         # Convert the input data into a DataFrame
#         campaign_data = pd.DataFrame([data])

#         # Use the loaded model to make predictions
#         prediction = model.predict(campaign_data)[0]

#         # Return the predicted fraud percentage as JSON
#         response = {"fraud_percentage": prediction}
#         return jsonify(response)
#     except Exception as e:
#         return jsonify({"error": str(e)}), 400

# if __name__ == "__main__":
    # app.run(debug=True)
    
    
#     import pickle

# # Assuming you've trained a model and stored it in a variable 'model'
# with open('fraud_detection_model.pkl', 'wb') as model_file:
#     pickle.dump(model, model_file)

