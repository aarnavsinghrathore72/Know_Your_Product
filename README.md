🧠 Know Your Product

This is an AI-powered product recognition and information app built using Streamlit and SerpAPI (Google Search API). It allows users to upload or capture product images and instantly get real-time information such as the product name, manufacturer, pricing, nutrition facts, and official links.
The main code for this app was developed by Aarnav Singh Rathore, in collaboration with contributors for various hackathons and science innovation projects.
________________________________________
🚀 Features

•	Image Upload or Camera Input: Upload or capture a product image directly from your webcam.

•	Product Recognition: Identifies the product and fetches relevant details using SerpAPI.

•	Company Information: Displays manufacturer details (e.g., Kellogg Company for Pringles).

•	Pricing & Availability: Shows pricing and redirects users to the product page or Pringles.com by default.

•	Nutrition Facts: Displays calories, fats, proteins, and other nutritional information.

•	Clean UI: Built with Streamlit for a simple and modern interface.
________________________________________
🧩 Requirements

The following Python libraries are required to run the app:

•	streamlit – For building the interactive web app

•	requests – For fetching data from the SerpAPI

•	pillow (PIL) – For image processing and display

•	python-dotenv (optional) – For managing your SerpAPI key securely

________________________________________
🧠 Usage

🖼️ Image Upload or Capture
Upload a product image or capture one using your device’s camera.

🔍 Product Recognition
The app will identify the product and display:
•	Product name & category
•	Description
•	Manufacturer (e.g., Kellogg Company for Pringles)
•	Website & official link

💰 Pricing & Availability
View current price listings and direct purchase links.
If a link isn’t available, the app automatically redirects to Pringles.com.

🍎 Nutrition Facts
Get key nutritional details such as calories, protein, and fat per serving.
________________________________________
🤖 Future Enhancements

•	🔍 OCR-based ingredient scanning (using Tesseract or EasyOCR)

•	📱 Barcode detection for faster product identification

•	🌱 Eco-impact rating system for sustainability awareness

•	🧩 Comparison mode for analyzing two products side by side

•	☁️ Cloud database integration for storing scanned products
________________________________________
💬 Acknowledgments

•	Aarnav Singh Rathore for the main code and concept development

•	Streamlit for providing the framework for rapid web app creation

•	SerpAPI for powering Google Search data retrieval

•	Kellogg Company / Pringles for sample product reference data


