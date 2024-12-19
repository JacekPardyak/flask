const csvFile = "bar-data.csv";

// Read the CSV file
d3.csv(csvFile).then(data => {
      // Print the data to the console
console.log("CSV Data:", data);

// Example: Iterate through and log each row
data.forEach(row => {
  console.log(`ID: ${row.id}, Name: ${row.name}, Value: ${row.value}`);
  });
 }).catch(error => {
    console.error("Error loading the CSV file:", error);
  });
  