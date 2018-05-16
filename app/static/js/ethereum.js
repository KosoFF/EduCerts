window.addEventListener('load', function () {


    // Now you can start your app & access web3 freely:
    //File reading error handler
    function fileErrorHandler(evt) {
        switch (evt.target.error.code) {
            case evt.target.error.NOT_FOUND_ERR:
                alert('File Not Found!');
                break;
            case evt.target.error.NOT_READABLE_ERR:
                alert('File is not readable');
                break;
            case evt.target.error.ABORT_ERR:
                break; // noop
            default:
                alert('An error occurred reading this file.');
        }

    }

    let progress = document.querySelector('.file-upload-progress-bar');

    function updateProgress(evt) {
        // evt is an ProgressEvent.
        if (evt.lengthComputable) {
            let percentLoaded = Math.round((evt.loaded / evt.total) * 100);
            // Increase the progress bar length.
            if (percentLoaded < 100) {
                progress.setAttribute('aria-valuenow', percentLoaded);
                progress.setAttribute('style', 'width: ' + percentLoaded + '%');
            }
        }
    }

    function fileOnload(evt) {
        if (evt.target.readyState !== 2) return;
        if (evt.target.error) {
            alert('Error while reading file');
            return;
        }

        t = evt.target.result;
        web3js.eth.sendTransaction({
            to: $('#ethereum_wallet').text(), value: 0,
            gas: 21000 + 68 * t.length + 10000, //just in case
            data: web3js.toHex(t)
        }, function (err, transactionHash) {
            if (!err)
                console.log(transactionHash); // "0x7f9fade1c0d57a7af66ab4ead7c2eb7b11a91385"
        });
    }


    send_json.addEventListener("click", function () {


        // Checking if Web3 has been injected by the browser (Mist/MetaMask)
        if (typeof web3 !== 'undefined') {
            // Use Mist/MetaMask's provider
            web3js = new Web3(web3.currentProvider);
        } else {
            // fallback - use your fallback strategy (local node / hosted node + in-dapp id mgmt / fail)
            $("#web3_error_modal").modal();
            return;
        }
        let networkID = web3js.version.network;
        if (networkID !== "3") {
            alert("Please, chose ropsten test network in your Web3 provider.");
            return;
        }
        let notLogged = false;
        web3js.eth.getAccounts(function (err, accounts) {
            if (err != null) console.error("An error occurred: " + err);
            else if (accounts.length === 0) {
                alert("User is not logged in to MetaMask");
                notLogged = true;
            }


        });
        if (notLogged)
            return;

        let reader = new FileReader();
        reader.onerror = fileErrorHandler;
        reader.onprogress = updateProgress;
        reader.onload = fileOnload;
        let file = document.getElementById('cert-file').files[0];
        reader.readAsText(file);


    });


});