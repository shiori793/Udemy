exports.getDate = () => {
    const options = {
        weekday: 'long',
        day: 'numeric',
        month: 'long'
    };

    const today = new Date();
    const day = today.toLocaleDateString('en-US', options);

    return day;
};

exports.getDay = () => {
    const options = {
        day: 'numeric'
    };

    const today = new Date();
    const day = today.toLocaleDateString('en-US', options);

    return day;
};