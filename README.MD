# Pre-training
This repository contains example code for using __typless__ ability of pre-learning.
Pre-learning ability allow developers to improve their customers experience.
To use it you must upload previous invoice files of customer with attaching confirmed data.
So for every row in database one request is should be done.
## Prerequisites
1. Register at [__typless__](https://developers.typless.com)
2. Log in
3. Click the _Settings_ tab in the side navigation bar to get API key
4. Create a new document type named _pre-learning-example_:
    * Click on the __Documents__ tab in the side navigation bar
    * Click on the __+New__ button
    * For the _name_ set "__pre-learning-example__"
    * For the _OCR language_ select "__English__"
    * Click on the __Next__ button
    * Leave fields as they are and click on the __Confirm__ button
5. Pre-learning ability is not enabled on free plan - [__contact us__](https://typless.com/#talk-to-an-expert) to enable it for testing
    
6. Get code of the example project from [__this__](https://github.com/typless/continuous_learning) Github repository.
    ```bash
    git clone https://github.com/typless/continuous_learning.git
    ```
    Set the API key:
    ```bash
    export API_KEY=YOUR_API_KEY_FROM_SETTINGS_TAB
    ```
    To install requirements:
    ```bash
    pip install -r requirements.txt
    ```
    To use pre-learning ability with example database:
    ```bash
    python pre_learning.py 
    ```
    
    To extract data from example invoice after pre-learning:
    ```bash
    python extract_data.py
    ```