curl -L -F "service=https://e-paper.nordbayern.de//ee/nn_sso/handler_ebookpdf.php" -F "page=authenticate" -F "inputLogin=XXXX" -F "inputPass=YYYYYY"  https://sso.nordbayern.de/oauth2/authorize.php?response_type=code^&state=xyz^&client_id=Tecnavia^&redirect_uri=https%%3A%%2F%%2Fe-paper.nordbayern.de%%2F%%2Fee%%2Fnn_sso%%2Fhandler_ebookpdf.php > output.txt

