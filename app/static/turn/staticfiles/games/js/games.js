$(window).on('load', function () {
    // enable dropdown once loaded
    $('#sort-dropdown').prop("disabled", false);
// Sort Dropdown script
    $("#sort-dropdown").change(function () {
        let sort, direction;
        // get the current url for reference
        let currentUrl = new URL(window.location);

        // get the dropdown element and its contents
        let selectionDropdown = $(this);
        let selectedVal = selectionDropdown.val();

        if (selectedVal !== "none") {
            // make a list of the values by their names
            let values = selectedVal.split("_");
            // set sort and direction accordingly
            if (values[0] !== 'positive') {
                sort = values[0];
                direction = values[1];
            } else {
                sort = `${values[0]}_${values[1]}`;
                direction = values[2];
            }
            // add the relevant search params to the url
            currentUrl.searchParams.set("sort", sort);
            currentUrl.searchParams.set("direction", direction);
            // reload with new url values
            window.location.replace(currentUrl);
        } else {
            // default to base url with no sorting
            currentUrl.searchParams.delete("sort");
            currentUrl.searchParams.delete("direction");

            window.location.replace(currentUrl);
        }
    });
});
