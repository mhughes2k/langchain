from typing import List

from langchain_core.callbacks import CallbackManagerForRetrieverRun, AsyncCallbackManagerForRetrieverRun
from langchain_core.documents import Document
from langchain_core.retrievers import BaseRetriever
# From Vector Stores
from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    ClassVar,
    Collection,
    Dict,
    Iterable,
    List,
    Optional,
    Tuple,
    Type,
    TypeVar,
)

from langchain_community.utilities.moodle import MoodleAPIWrapper

class MoodleRetriever(BaseRetriever, MoodleAPIWrapper):
    """ Moodle Retriever

    Really a wrapper around a vector store database, with
    a Moodle security access layer.
    """

    def _get_relevant_documents(
            self,
            query: str, *, run_manager: CallbackManagerForRetrieverRun
    ) -> List[Document]:
        docs = super()._get_relevant_documents(self, query, run_manager=run_manager)
        # TODO Implement Moodle security checks
        return docs

    async def _aget_relevant_documents(
        self, query: str, *, run_manager: AsyncCallbackManagerForRetrieverRun
    ) -> List[Document]:
        docs = super()._aget_relevant_documents(self, query, run_manager=run_manager)


