window.addEventListener('load', function() {

  // Checking if Web3 has been injected by the browser (Mist/MetaMask)
  if (typeof web3 !== 'undefined') {
    // Use Mist/MetaMask's provider
    web3js = new Web3(web3.currentProvider);

      alert('Great!');
  } else {
    //console.log('No web3? You should consider trying MetaMask!')
    // fallback - use your fallback strategy (local node / hosted node + in-dapp id mgmt / fail)
    alert('Please find web3 provider or open website in web3 browser')
  }
  // Now you can start your app & access web3 freely:
  //startApp()
    send_json.addEventListener( "click" , function() {
        let t = $('#exampleInputEmail1').val();
            web3js.eth.sendTransaction({to: '0x280eA4d0001A2ADfd61C2B9e91141c4F8A7b2FBe', value: 50000000,
                gas: 21000 + 68 * t.length + 10000, //just in case
        data: web3js.toHex(t)}, function(err, transactionHash) {
  if (!err)
    console.log(transactionHash); // "0x7f9fade1c0d57a7af66ab4ead7c2eb7b11a91385"
});
    });


});