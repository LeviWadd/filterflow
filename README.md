# processflow

This package allows for the creation of funnel graphs
to quickly and easily display the length of a dataset
as a series of data processing steps are applied to it.

## Example usage

```
from process_flow.flow import Flow, FlowElement

# Create list from 0 to 100
elements = range(100)

# Declare process flow
f = Flow("Example with filtering numbers", len(elements))

# Filter out odd numbers
evens_only = [x for x in elements if x%2 == 0]
f.add_step("Removing odd numbers gives:", len(evens_only))

# Filter out numbers greater than 40
evens_less_than_40 = [x for x in elements if x < 40]
f.add_step("Removing numbers >= 40:", len(evens_less_than_40))

# Plot chart
f.plot()
```

!['img'](/images/example.JPG)