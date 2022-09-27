fetch(PAYMENTS_KEY_URL)
  .then((result) => { return result.json(); })
  .then((data) => {
    // Initialize Stripe.js
    const stripe = Stripe(data.publicKey);

    document.querySelector("#submitBtn").addEventListener("click", () => {
      const quantityElem = document.querySelector('input[name=quantity_a]');
      const quantity_a = parseInt(quantityElem.value, 10);
      const quantityElem1 = document.querySelector('input[name=quantity_ch]');
      const quantity_ch = parseInt(quantityElem1.value, 10);
  

      // Get Checkout Session ID
      fetch(`${PAYMENTS_CHECKOUT_SESSION_URL}?quantity_a=${quantity_a}&quantity_ch=${quantity_ch}`)
      .then((result) => {
          if (result.status >= 200 && result.status <= 299) {
            return Promise.resolve(result.json());
          } else {
            return Promise.reject(result.json());
          }
       })
      .then((data) => {
        console.log(data);
        // Redirect to Stripe Checkout
        return stripe.redirectToCheckout({sessionId: data.sessionId})
      })
      .then((res) => {
        console.log(res);
      }).catch(err => {
        console.error("THERE WAS AN ERROR!");
      });
    });

  });
