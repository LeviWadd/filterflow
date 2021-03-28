from typing import List, Union

from plotly.graph_objects import Figure, Funnel

class FlowElement:
    """
    A class representing individual steps to be visualised
    in the process chart.

    ...

    Attributes
    ----------
    value : Union[int, float]
        The value of the data after the processing step.
    title : str
        A string describing the processing step.
    """

    def __init__(self, title: str, value: Union[int, float]):
        """
        Initialiser for FlowElement class.

        Parameters
        ----------
        title : str
            A string describing the processing step.
        value : Union[int, float]
            The value of the data after the processing step.
        """
        self.value = value
        self.title = title

    def __str__(self):
        return str({self.title, self.value})

    def __repr__(self):
        return self.__str__()

class Flow:
    """
    A class to represent the full flow of our process to
    be visualised.

    ...

    Attributes
    ----------
    title : str
        The title of the process flow plot.
    initial_val : Union[int, float]
        The starting length of the dataset before any
        of the process flow steps have taken place.
    steps : List[FlowElement], optional
        The data processing steps, by default [].

    Methods
    -------
    add_step(title, value)
        Adds a data processing step.
    plot(font_size=18)
        Creates a funnel plot of the data processing flow using plotly.
    """

    def __init__(self, title: str, initial_val: Union[int, float]):
        """
        Initialiser for Flow class.

        Parameters
        ----------
        title : str
            The title of the process flow plot.
        initial_val : Union[int, float]
            The starting length of the dataset before any
            of the process flow steps have taken place.
        steps : List[FlowElement], optional
            The data processing steps, by default [].
        """
        self.title = title
        self.initial_val = initial_val
        self.steps = []
        self.fig = None

    def add_step(self, title: str, value: Union[int, float]):
        """
        Add a step to the process flow.

        Parameters
        ----------
        title : str
            The title of the process step.
        value : Union[int, float]
            The length of the data after the process step.
        """
        el = FlowElement(title, value)
        self.steps.append(el)

    def __str__(self):
        return (
            f"Title: '{self.title}'\n"
            f"Initial value: '{self.initial_val}'\n"
            f"Elements: {self.steps}")

    def __repr__(self):
        return self.__str__()

    def plot(self,
        font_size: int = 18,
        figure_kwargs = {},
        funnel_kwargs = {},
        update_layout_kwargs = {}):
        """
        Plots a funnel graph depicting the process flow.

        Parameters
        ----------
        font_size : int, optional
            The font size for the plots, by default 18
        figure_kwargs : dict, optional
            The keyword-arguments passed to go.Figure(), by default {}
        funnel_kwargs : dict, optional
            The keyword-arguments passed to go.Funnel(), by default {}
        update_layout_kwargs : dict, optional
            The keyword-arguments passed to the update_layout call, by default {}

        Returns
        -------
        go.Figure
            Figure showing the flow of data processing steps.
        """
        self.fig = Figure(
            Funnel(
                name = self.title,
                orientation = "h",
                y = ["Start  "] + [f"{el.title}  " for el in self.steps],
                x = [self.initial_val] + [el.value for el in self.steps],
                textposition = "inside",
                texttemplate = "n = %{x}",
                **funnel_kwargs,
            ),
            **figure_kwargs,
        )

        self.fig.update_layout(
            title = self.title,
            font=dict(
                size=font_size,
            ),
            **update_layout_kwargs,
        )

        return self.fig