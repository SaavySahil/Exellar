;(function () {
  'use strict';

  var CARDS_PER_PAGE = 8;
  var currentPage = 1;
  var activeStatus = null; // null=all, 'ongoing', 'completed'

  function getAllCards() {
    return Array.prototype.slice.call(
      document.querySelectorAll('.project-list-holder [data-status]')
    );
  }

  function getFilteredCards() {
    var cards = getAllCards();
    if (!activeStatus) return cards;
    return cards.filter(function (c) {
      return c.getAttribute('data-status') === activeStatus;
    });
  }

  function renderPage(page) {
    currentPage = page;
    var filtered = getFilteredCards();
    var all = getAllCards();

    // Hide all
    all.forEach(function (c) { c.style.display = 'none'; });

    // Show page slice
    var start = (page - 1) * CARDS_PER_PAGE;
    filtered.slice(start, start + CARDS_PER_PAGE).forEach(function (c) {
      c.style.display = '';
    });

    updatePagination(filtered.length);
  }

  function updatePagination(total) {
    var numContainer = document.getElementById('proj-paging-nums');
    var nextBtn      = document.getElementById('proj-next-btn');
    var paginWrap    = document.getElementById('proj-pagination-wrap');

    if (!numContainer) return;

    var totalPages = Math.ceil(total / CARDS_PER_PAGE);

    // Show/hide whole pagination block
    if (paginWrap) {
      paginWrap.style.display = totalPages > 1 ? '' : 'none';
    }

    // Rebuild page number links
    numContainer.innerHTML = '';
    for (var i = 1; i <= totalPages; i++) {
      var a = document.createElement('a');
      a.textContent = i;
      a.href = '#';
      a.className = i === currentPage ? 'active' : '';
      (function (p) {
        a.addEventListener('click', function (e) {
          e.preventDefault();
          renderPage(p);
          var sec = document.querySelector('.proj-holder-replace');
          if (sec) sec.scrollIntoView({ behavior: 'smooth' });
        });
      })(i);
      numContainer.appendChild(a);
    }

    // Next page button
    if (nextBtn) {
      if (currentPage < totalPages) {
        nextBtn.style.display = '';
        nextBtn.onclick = function (e) {
          e.preventDefault();
          renderPage(currentPage + 1);
          var sec = document.querySelector('.proj-holder-replace');
          if (sec) sec.scrollIntoView({ behavior: 'smooth' });
        };
      } else {
        nextBtn.style.display = 'none';
      }
    }
  }

  function applyStatusFilter() {
    var ongoingCb  = document.getElementById('filter-ongoing');
    var completedCb = document.getElementById('filter-completed');
    if (!ongoingCb || !completedCb) return;

    var onChecked = ongoingCb.checked;
    var coChecked = completedCb.checked;

    if (onChecked && !coChecked) {
      activeStatus = 'ongoing';
    } else if (!onChecked && coChecked) {
      activeStatus = 'completed';
    } else {
      activeStatus = null; // both checked or neither = show all
    }

    renderPage(1);
  }

  function init() {
    var ongoingCb  = document.getElementById('filter-ongoing');
    var completedCb = document.getElementById('filter-completed');
    if (ongoingCb)  ongoingCb.addEventListener('change', applyStatusFilter);
    if (completedCb) completedCb.addEventListener('change', applyStatusFilter);

    renderPage(1);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
