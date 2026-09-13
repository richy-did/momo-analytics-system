const summaryGrid = document.getElementById('summaryGrid');
const transactionTableBody = document.getElementById('transactionTableBody');
const categoryChart = document.getElementById('categoryChart');
const reloadButton = document.getElementById('reloadButton');

async function loadDashboard() {
  try {
    const response = await fetch('./data/processed/dashboard.json');
    if (!response.ok) {
      throw new Error('dashboard file not found');
    }

    const data = await response.json();
    renderSummary(data.summary || []);
    renderCategories(data.categories || []);
    renderTransactions(data.transactions || []);
  } catch (error) {
    summaryGrid.innerHTML = '<div class="summary-card"><span class="label">Status</span><span class="value">No data</span></div>';
    transactionTableBody.innerHTML = '<tr><td colspan="5">Run the ETL job to generate dashboard data.</td></tr>';
    categoryChart.innerHTML = '<p>Dashboard data not available yet.</p>';
    console.error(error);
  }
}

function renderSummary(summary) {
  summaryGrid.innerHTML = summary
    .map(
      (item) => `
        <div class="summary-card">
          <span class="label">${item.label}</span>
          <span class="value">${item.value}</span>
        </div>
      `
    )
    .join('');
}

function renderCategories(categories) {
  if (!categories.length) {
    categoryChart.innerHTML = '<p>No category data available.</p>';
    return;
  }

  const max = Math.max(...categories.map((item) => item.value));

  categoryChart.innerHTML = categories
    .map((item) => {
      const height = max === 0 ? 20 : (item.value / max) * 100;
      return `
        <div class="bar" style="height:${height}%">
          ${item.label}<br>${item.value}
        </div>
      `;
    })
    .join('');
}

function renderTransactions(transactions) {
  if (!transactions.length) {
    transactionTableBody.innerHTML = '<tr><td colspan="5">No transactions found.</td></tr>';
    return;
  }

  transactionTableBody.innerHTML = transactions
    .slice(0, 10)
    .map(
      (tx) => `
        <tr>
          <td>${tx.date}</td>
          <td>${tx.type}</td>
          <td>${tx.amount}</td>
          <td>${tx.phone}</td>
          <td>${tx.channel}</td>
        </tr>
      `
    )
    .join('');
}

reloadButton.addEventListener('click', loadDashboard);
loadDashboard();
