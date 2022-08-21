// Get the keys from the context passed json
let stripePublicKey = $("#id_stripe_public_key").text().slice(1, -1);
let clientSecret = $("#id_client_secret").text().slice(1, -1);

// init stripe
let stripe = Stripe(stripePublicKey);
// init the stripe elements
let elements = stripe.elements();

// update the cards styling to match the site
let style = {
    base: {
        color: "#000",
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: "antialiased",
        fontSize: "16px",
        "::placeholder": {
            color: "#dbdbdb",
        },
    },
    invalid: {
        color: "#f14668",
        iconColor: "#f14668",
    },
};

// create a card element
let card = elements.create("card", {style: style});
// mount the card element to the div in the payment view
card.mount("#card-element");

// Display realtime validation errors on the card element
card.addEventListener("change", function (event) {
    let errorDiv = document.getElementById("card-errors");
    if (event.error) {
        let html = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${event.error.message}</span>
        `;
        $(errorDiv).html(html);
        $(errorDiv).addClass("help");
    } else {
        errorDiv.textContent = "";
    }
});

// Handle form submission
let paymentForm = document.getElementById('payment-form');

paymentForm.addEventListener('submit', function (event) {
    // stop POST submit
    event.preventDefault();
    // stop multiple submits
    // disable card element
    card.update({'disabled': true});
    // trigger loading button
    $('#submit-payment-button').addClass("is-loading");
    // disable the button
    $('#submit-payment-button').attr('disabled', true);

    // capture form data
    let csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    let postData = {
        'csrfmiddlewaretoken': csrfToken,
        'client_secret': clientSecret,
    };

    // cache order url
    let url = '/checkout/cache_checkout_data/';

    $.post(url, postData).done(function () {
        // confirm the payment
        stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: card,
                billing_details: {
                    name: $.trim(paymentForm.full_name.value),
                    email: $.trim(paymentForm.email.value),
                    phone: $.trim(paymentForm.phone_number.value),
                    address: {
                        line1: $.trim(paymentForm.street_address1.value),
                        line2: $.trim(paymentForm.street_address2.value),
                        city: $.trim(paymentForm.town_or_city.value),
                        country: $.trim(paymentForm.country.value),
                        state: $.trim(paymentForm.county.value),
                    }
                },
            },
        }).then(function (result) {
            if (result.error) {
                // Show error to customer
                let errorDiv = document.getElementById('card-errors');
                let html = `
                    <span class="icon" role="alert">
                    <i class="fas fa-times"></i>
                    </span>
                    <span>${result.error.message}</span>`;
                $(errorDiv).html(html);
                // enable element
                card.update({'disabled': false});
                // remove loading class
                $('#submit-payment-button').removeClass('is-loading');
                // enable submit button
                $('#submit-payment-button').attr('disabled', false);
            } else {
                if (result.paymentIntent.status === 'succeeded') {
                    // successful - submit the form
                    paymentForm.submit();
                }
            }
        });
    }).fail(function () {
        // reload the page if all else fails
        location.reload();
    });
});




