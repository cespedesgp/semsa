from dash.html import Div, H3, I, P

class Painel:
  def __init__(self, title, description):
    self.title = title
    self.description = description


def make_card1(painel):
  return Div(
    className="card",
    children=[
      Div(
        className="face face1",
        children=Div(
          className="content",
          children=Div(
            className="icon",
            children=[
              H3(
                children=painel.title
              ),
              I(
              className="fa",
              **{'aria-hidden':"true"}
            )]
          )
        )
      ),
      Div(
        className="face face2",
        children=Div(
          className="content",
          children=[H3(
            children=painel.title
          ),
          P(
            children=painel.description
          )]
        )
      )]
  )


layout = Div(
  className="container",
  children=make_card1(Painel("Painel 1","Descrição painel 1"))
)