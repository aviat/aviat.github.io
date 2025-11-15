document.addEventListener('DOMContentLoaded', function() {
    const filterGroups = document.querySelectorAll('.filter-buttons');
    const portfolioItems = document.querySelectorAll('.portfolio-item');

    filterGroups.forEach(group => {
        const filterType = group.dataset.filter;
        const buttons = group.querySelectorAll('.filter-btn');

        buttons.forEach(button => {
            button.addEventListener('click', () => {
                // Update active state
                buttons.forEach(btn => btn.classList.remove('active'));
                button.classList.add('active');

                // Get all active filters
                const activeFilters = {};
                document.querySelectorAll('.filter-buttons').forEach(filterGroup => {
                    const type = filterGroup.dataset.filter;
                    const activeBtn = filterGroup.querySelector('.filter-btn.active');
                    activeFilters[type] = activeBtn.dataset.value;
                });

                // Filter items
                portfolioItems.forEach(item => {
                    let show = true;

                    // Check each filter type
                    Object.entries(activeFilters).forEach(([type, value]) => {
                        if (value !== 'all' && item.dataset[type] !== value) {
                            show = false;
                        }
                    });

                    // Show/hide item
                    item.style.display = show ? 'block' : 'none';
                });
            });
        });
    });
});
