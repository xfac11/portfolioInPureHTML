document.querySelectorAll('[data-include]').forEach(async (placeholder) => {
    try {
        const response = await fetch(placeholder.dataset.include);
        if (!response.ok) {
            throw new Error(`Could not load ${placeholder.dataset.include}`);
        }
        placeholder.outerHTML = await response.text();
    } catch (error) {
        console.error(error);
    }
});
