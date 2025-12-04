// Shared parking functionality

// Calculate availability for a parking lot
function getLotAvailability(lotName) {
    let available = 0;
    let total = 0;
    
    // Count spots (assuming 10 spots per lot, can be made dynamic)
    for (let i = 1; i <= 10; i++) {
        total++;
        const key = `${lotName}-spot-${i}`;
        const status = localStorage.getItem(key);
        if (status !== "occupied") {
            available++;
        }
    }
    
    return { available, total };
}

// Update availability display
function updateAvailabilityDisplay(lotName, elementId) {
    const stats = getLotAvailability(lotName);
    const element = document.getElementById(elementId);
    if (element) {
        element.textContent = `${stats.available} of ${stats.total} available`;
    }
    return stats;
}

// Show toast notification
function showToast(message, type = 'info') {
    // Remove existing toast if any
    const existingToast = document.querySelector('.toast');
    if (existingToast) {
        existingToast.remove();
    }
    
    // Create toast element
    const toast = document.createElement('div');
    toast.className = `toast toast-${type}`;
    toast.textContent = message;
    
    // Add styles
    toast.style.cssText = `
        position: fixed;
        bottom: 2rem;
        left: 50%;
        transform: translateX(-50%) translateY(100px);
        background: ${type === 'success' ? '#34c759' : type === 'error' ? '#ff3b30' : '#0071e3'};
        color: white;
        padding: 0.875rem 1.5rem;
        border-radius: 980px;
        font-size: 0.9375rem;
        font-weight: 400;
        z-index: 1000;
        opacity: 0;
        transition: all 0.4s cubic-bezier(0.28, 0.11, 0.32, 1);
        pointer-events: none;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
    `;
    
    document.body.appendChild(toast);
    
    // Animate in
    requestAnimationFrame(() => {
        toast.style.transform = 'translateX(-50%) translateY(0)';
        toast.style.opacity = '1';
    });
    
    // Remove after delay
    setTimeout(() => {
        toast.style.transform = 'translateX(-50%) translateY(100px)';
        toast.style.opacity = '0';
        setTimeout(() => toast.remove(), 400);
    }, 2000);
}

// Initialize parking spots with enhanced functionality
function initParkingSpots(lotName, onUpdate) {
    document.querySelectorAll(".spot").forEach(spot => {
        const num = spot.dataset.number;
        const key = `${lotName}-spot-${num}`;
        const saved = localStorage.getItem(key);

        if (saved === "occupied") {
            spot.classList.add("occupied");
        }

        spot.addEventListener("click", () => {
            const wasOccupied = spot.classList.contains("occupied");
            spot.classList.toggle("occupied");

            if (spot.classList.contains("occupied")) {
                localStorage.setItem(key, "occupied");
                showToast(`Spot ${num} marked as occupied`, 'info');
            } else {
                localStorage.setItem(key, "empty");
                showToast(`Spot ${num} marked as available`, 'success');
            }
            
            // Callback for updating counters
            if (onUpdate) {
                onUpdate();
            }
        });
    });
}

