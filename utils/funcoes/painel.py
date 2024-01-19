def make_card(painel):
  return html.Div(
    className="card",
    children=[
      html.Div(
        className="face face1",
        children=html.Div(
          className="content",
          children=html.Div(
            className="icon",
            children=[
              html.H3(
                children=painel.title
              ),
              html.I(
              className="fa",
              **{'aria-hidden':"true"}
            )]
          )
        )
      ),
      html.Div(
        className="face face2",
        children=html.Div(
          className="content",
          children=[html.H3(
            children=painel.title
          ),
          html.P(
            children=painel.description
          )]
        )
      )]
  )

